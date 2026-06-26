const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..');
const required = [
  'README.md',
  'package.json',
  'themes/hmg.css',
  'examples/hmg-sample.md',
  'examples/hmg-wide.md',
  'docs/reference.md',
  'assets/hmg-template-media/image1.png'
];

let failures = [];
for (const rel of required) {
  const full = path.join(root, rel);
  if (!fs.existsSync(full)) failures.push(`Missing required file: ${rel}`);
}

const css = fs.readFileSync(path.join(root, 'themes/hmg.css'), 'utf8');
for (const token of ['/* @theme hmg */', '--hmg-navy: #002c5f', '--hmg-logo: url', 'section.cover .cover-purpose', 'section.cover .cover-meta', 'section.diagram', 'section.dense', '.code-split', '.process', '.cards', '.columns-2-1']) {
  if (!css.includes(token)) failures.push(`Theme CSS missing token: ${token}`);
}

for (const deck of ['examples/hmg-sample.md', 'examples/hmg-wide.md']) {
  const md = fs.readFileSync(path.join(root, deck), 'utf8');
  for (const token of ['marp: true', 'theme: hmg']) {
    if (!md.includes(token)) failures.push(`${deck} missing token: ${token}`);
  }
}

if (failures.length) {
  console.error(failures.join('\n'));
  process.exit(1);
}
console.log('Validation passed: required files, theme tokens, and sample deck frontmatter are present.');
