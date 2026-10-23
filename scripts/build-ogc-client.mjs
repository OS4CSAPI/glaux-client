import { execFileSync } from 'node:child_process';
import { globSync, rmSync } from 'node:fs';
import { createRequire } from 'node:module';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const library = join(root, '.dependencies', 'ogc-client');
const expected = '4ca1d7db9b1ccdf545adbef42ef941139fe11977';
const actual = execFileSync('git', ['-C', library, 'rev-parse', 'HEAD'], {
  encoding: 'utf8',
}).trim();
if (actual !== expected) {
  throw new Error(`Unexpected ogc-client revision ${actual}; expected ${expected}. See docs/DEPENDENCIES.md.`);
}
if (execFileSync('git', ['-C', library, 'status', '--porcelain', '--untracked-files=no'], {
  encoding: 'utf8',
}).trim()) {
  throw new Error('The ogc-client submodule has modified tracked files; refusing to build an unverified dependency.');
}

const npm = process.env.npm_execpath;
if (!npm) {
  throw new Error('Run this build through npm (npm ci or npm run postinstall).');
}
function runNpm(...args) {
  execFileSync(process.execPath, [npm, ...args], { cwd: library, stdio: 'inherit' });
}

runNpm('ci', '--no-audit', '--no-fund');
rmSync(join(library, 'dist'), { recursive: true, force: true });
runNpm('run', 'build:worker');
runNpm('run', 'build:node');

// Equivalent to upstream build:browser, without POSIX find/rm requirements on Windows.
const require = createRequire(join(library, 'package.json'));
const { build } = require('esbuild');
await build({
  absWorkingDir: library,
  entryPoints: Array.from(globSync('src/**/*.ts', {
    cwd: library,
    exclude: ['src/**/*.spec.ts', 'src/worker/index.ts'],
  })),
  outdir: 'dist',
  platform: 'neutral',
  format: 'esm',
  sourcemap: true,
});
console.log(`Built pinned ogc-client ${actual}`);
