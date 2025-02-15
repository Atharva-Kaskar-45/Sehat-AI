import arrow from '../assets/arrow.svg'
import heroImage from "../assets/hero_image.jpg"
const Hero = ()=>{
    return(
        <section className="flex">
            <div className="px-42 py-28 ">
                <h1 className="text-white text-4xl w-[250px] py-2"><span className=" bg-gradient-to-bl from-[#AAD9D1] to-[#017373] bg-clip-text text-transparent">
                    Your</span> Smart Companion for Better <span className="text-[#017373]">Health</span> & Well-Being!
                </h1>
                <p className="text-white pb-6 pt-2">Empowering You with AI-Driven Health Insights & Personalized Care.</p>
                <div className="flex justify-between bg-white w-[434px] p-1 rounded">
                    <input className="w-full" placeholder="Enter your email">
                    </input>
                    <button className="bg-gradient-to-bl from-[#AAD9D1] to-[#017373] text-black w-[180px] h-[56px]  px-6 py-2 rounded-[8px] hover:scale-102 flex items-center gap-2 hover:cursor-pointer">Sign Up
                    <img src={arrow} className=" border-2 border-solid border-black w-4 h-4 ml-2"></img>
                    </button>
                </div>
            </div>
            <div>
                <div className="w-[570px] p-4">
                <img src={heroImage}></img>
                </div>
            </div>
        </section>
    )
}
export default Hero