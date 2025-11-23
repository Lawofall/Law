import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// 获取仓库名称（用于GitHub Pages部署）
// 如果您的仓库名是 "Law"，则 base 应该是 "/Law/"
// 如果您的仓库名是 "law-website"，则 base 应该是 "/law-website/"
// 请根据您的实际仓库名修改下面的值
const repoName = process.env.GITHUB_REPOSITORY?.split('/')[1] || 'Law' // 默认值，请修改为您的仓库名

export default defineConfig({
  plugins: [react()],
  base: process.env.NODE_ENV === 'production' ? `/${repoName}/` : '/',
  server: {
    port: 3000,
    open: true
  }
})



