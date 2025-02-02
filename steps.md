# update Node and export path
- brew install node@22  
- export ""
- source ~/.zshrc    

# create Vite, install packages
- npm create vite@latest my-vite-app --template react-ts 
- npm install
- npm run dev

# install tailwind
- npm install -D tailwindcss
- npx tailwindcss init  

# update tailwind config
`
content: [
    "./src/**/*.(js,jsx,tsx,tsx)"
  ]
`

# add tailwind css
`
/* src/index.css */
@tailwind base;
@tailwind components;
@tailwind utilities;
`

# create postcss.config.mjs
`
export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
};

`

# install dev dependencies
npm install -D @types/react @types/react-dom @types/react-router-dom\n
npm install -D prettier prettier-plugin-tailwindcss

# install react-router-dom
npm install react-router-dom

