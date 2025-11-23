# GitHub Pages 空白页问题修复说明

## 问题原因

GitHub Pages 空白页通常是因为：
1. **路径配置错误**：GitHub Pages 的路径格式是 `username.github.io/repo-name/`，需要在 Vite 配置中设置正确的 base 路径
2. **路由问题**：React Router 的 BrowserRouter 需要配置 basename
3. **404 重定向**：GitHub Pages 不支持客户端路由，需要 404.html 处理

## 已修复的文件

### 1. `vite.config.js`
- 添加了 `base` 配置，用于生产环境的路径前缀
- **重要**：请将 `repoName` 变量修改为您的实际仓库名

### 2. `src/App.jsx`
- 为 `BrowserRouter` 添加了 `basename` 属性
- **重要**：请将 `repoName` 变量修改为您的实际仓库名

### 3. `public/404.html`
- 创建了 404.html 文件，用于处理路由重定向

## 修复步骤

### 步骤 1：修改仓库名

1. 打开 `vite.config.js`，找到这一行：
   ```javascript
   const repoName = process.env.GITHUB_REPOSITORY?.split('/')[1] || 'Law' // 默认值，请修改为您的仓库名
   ```
   将 `'Law'` 改为您的实际仓库名（例如：`'law-website'`）

2. 打开 `src/App.jsx`，找到这一行：
   ```javascript
   const repoName = 'Law' // 默认值，请修改为您的实际仓库名
   ```
   将 `'Law'` 改为您的实际仓库名（与上面保持一致）

### 步骤 2：重新构建和部署

```bash
# 1. 清理旧的构建文件
rm -rf dist

# 2. 重新构建
npm run build

# 3. 如果使用 gh-pages 部署
npm run deploy

# 或者手动部署：
# 将 dist 文件夹的内容复制到 gh-pages 分支
```

### 步骤 3：检查 GitHub Pages 设置

1. 在 GitHub 仓库中，进入 **Settings** → **Pages**
2. 确保 **Source** 选择的是 `gh-pages` 分支（或您使用的分支）
3. 确保 **Branch** 选择的是 `/ (root)` 或 `/docs`

## 如何找到您的仓库名？

1. 访问您的 GitHub 仓库页面
2. 查看 URL，格式是：`https://github.com/username/repo-name`
3. `repo-name` 就是您的仓库名

例如：
- URL: `https://github.com/yourname/Law`
- 仓库名: `Law`

- URL: `https://github.com/yourname/law-website`
- 仓库名: `law-website`

## 验证修复

部署完成后，访问您的 GitHub Pages 网址：
- 格式：`https://your-username.github.io/repo-name/`
- 应该能看到网站正常显示

## 如果还是空白？

1. **检查浏览器控制台**（F12）：
   - 查看是否有 404 错误
   - 查看是否有路径错误

2. **检查构建文件**：
   - 确保 `dist/index.html` 存在
   - 确保所有资源文件都在 `dist` 文件夹中

3. **检查路径**：
   - 确保 `vite.config.js` 和 `App.jsx` 中的 `repoName` 都正确
   - 确保路径格式是 `/repo-name/`（注意前后都有斜杠）

4. **清除缓存**：
   - 浏览器按 Ctrl+Shift+R（Windows）或 Cmd+Shift+R（Mac）强制刷新

## 常见问题

### Q: 如何知道我的仓库名？
A: 查看 GitHub 仓库的 URL，最后一部分就是仓库名。

### Q: 仓库名区分大小写吗？
A: GitHub 仓库名不区分大小写，但建议使用小写。

### Q: 修改后需要重新部署吗？
A: 是的，修改配置后需要重新运行 `npm run build` 和部署。

### Q: 可以使用自定义域名吗？
A: 可以，在 GitHub Pages 设置中添加自定义域名即可。

## 完成！

修复完成后，您的网站应该可以正常访问了！

如果还有问题，请检查：
1. 浏览器控制台的错误信息
2. GitHub Pages 的部署日志
3. 确保所有文件都已正确提交到仓库

