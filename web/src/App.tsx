import { Button } from '@/components/ui/button'
import { ThemeProvider } from '@/components/theme-provider'
import { lere } from '@lere/core'

function App() {
  const onClick = () => {
    console.log(lere)
  }
  return (
    <ThemeProvider defaultTheme="dark" storageKey="vite-ui-theme">
      <div className="h-dvh flex flex-col items-center justify-center gap-4 w-full">
        <h1 className="text-3xl font-bold underline">Hello world!</h1>
        <Button onClick={onClick}>Click me</Button>
      </div>
    </ThemeProvider>
  )
}

export default App
