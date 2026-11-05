// node render.js -> PDF + overflow report + page PNGs for review
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const dir = __dirname;
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 900, height: 1200 } });
  await page.goto('file://' + path.join(dir, 'operators-curriculum.html'), { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  const report = await page.evaluate(() => [...document.querySelectorAll('.page')].map((p, i) => {
    // content overflow: any child extending below footer zone
    const pr = p.getBoundingClientRect();
    let maxBottom = 0;
    p.querySelectorAll(':scope > *:not(.pf)').forEach(c => { maxBottom = Math.max(maxBottom, c.getBoundingClientRect().bottom - pr.top); });
    const limit = pr.height - (20 * 96 / 25.4) + 4; // bottom padding 20mm
    return { page: i + 1, used: Math.round(maxBottom), limit: Math.round(limit), over: maxBottom > limit };
  }));
  console.log(JSON.stringify(report));
  const fonts = await page.evaluate(() => [...document.fonts].filter(f => f.status === 'loaded').map(f => f.family + ' ' + f.weight + ' ' + f.style));
  console.log('fonts loaded:', [...new Set(fonts)].join(' | '));
  await page.pdf({ path: path.join(dir, 'akitsuu-Operators-Curriculum.pdf'), format: 'A4', printBackground: true, preferCSSPageSize: true });
  if (process.argv[2] === 'shots') {
    const n = report.length;
    for (let i = 0; i < n; i++) {
      const el = (await page.$$('.page'))[i];
      await el.screenshot({ path: path.join(process.argv[3] || dir, `p${String(i + 1).padStart(2, '0')}.png`) });
    }
  }
  await browser.close();
})();
