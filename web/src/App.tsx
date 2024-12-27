import './App.css'
import { Button } from '@/components/ui/button'
import { ThemeProvider } from "@/components/theme-provider"

function App() {
  return (
    <ThemeProvider defaultTheme="dark" storageKey="vite-ui-theme">
      <div className='h-dvh flex flex-col items-center justify-center gap-4'>
        <h1 className="text-3xl font-bold underline">
          Hello world!
        </h1>
        <Button>Click me</Button>
      </div>
    </ThemeProvider>
  )
}

export default App
