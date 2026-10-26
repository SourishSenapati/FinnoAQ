import { defineConfig } from 'vite';

export default defineConfig({
  root: './',
  publicDir: 'public',
  build: {
    outDir: 'dist',
    emptyOutDir: true,
    chunkSizeWarningLimit: 1000,
    rollupOptions: {
      output: {
        manualChunks(id) {
          if (id.includes('three')) {
            return 'vendor-three';
          }
        }
      }
    }
  },
  server: {
    port: 5173,
    open: false
  },
  preview: {
    port: 5173
  }
});
