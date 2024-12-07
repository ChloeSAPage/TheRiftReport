import './App.css'
import lolBg from './assets/lol-bg.jpg'

function App() {

  return (
      <section>
        <div className="nav-bar font-inter font-medium">
          <p className="container mx-auto">
            The Rift Report
          </p>
        </div>
        <div className="container mx-auto my-5 px-64">
          <div>
            <div>
              <h1 className='font-bold text-2xl font-inter w-2/3'>Wondering about the newest League patch?</h1>
            </div>
            <div className="flex justify-end">
              <h1 className='font-bold text-2xl font-inter w-2/3 text-right'>
              Or what is trending on X? <br></br>Or Reddit?</h1>
            </div>
            <div className="flex justify-center mt-3">
              <img src={lolBg} alt="placeholder" className="w-full h-72 object-cover" />
            </div>
          </div>
        </div>
      </section>
  )
}

export default App
