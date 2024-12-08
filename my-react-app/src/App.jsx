import './App.css'
import lolBg from './assets/lol-bg.jpg'
import logo from './assets/rift-report-logo.png'

function App() {
  return (
    <section>
      <div className="nav-bar h-16 flex items-center">
        <img src={logo} className="h-full object-contain ml-2"></img>
        <p className="container mx-auto font-futura font-medium bg-black my-3 ml-3">
          The Rift Report
        </p>
      </div>
      <div className="w-full h-[300px] relative">
        <img src={lolBg} alt="banner" className="w-full h-full object-cover brightness-50"/>
        <div className="absolute px-32 flex top-0 bottom-0 items-center justify-center w-full flex-col">
          <img src={logo} className="h-[150px]"></img>
        </div>
      </div>
      <div className="px-32">
        <div className="container mx-auto p-5 bg-white">
          <h1 className='font-bold text-xl font-futura w-3/5 mb-4'>
            Latest Patch Summary:
          </h1>
          <p>
            The latest patch has brought a lot of changes to the game. 
            <br></br>
            The meta has shifted and new champions are now in the spotlight.
            <br></br> 
            Here are some of the highlights:
            <br></br>
            Ivern is in the dirt
            <br></br>
            Azir is still in the dirt
            <br></br>
            No one saw this coming
            <br></br>
            Woah
          </p>
        </div>
      </div>
    </section>
  )
}

export default App;
