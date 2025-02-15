import facebook from '../assets/facebook.svg'
import twitter from '../assets/twitter.svg'
import youtube from '../assets/youtube.svg'
import linkedin from '../assets/linkedin.svg'
import logo from '../assets/SehatAI_logo.jpg'
import arrow from '../assets/arrow.svg'
const Footer = ()=>{
    return(
        <>
        <div className='flex border-t-1 border-[#048C80]/50'>
        <div className="flex flex-col py-[80px] px-[144px]">
            <div className='flex py-[50px]'>
            <img src={logo} width={48} className="rounded"></img>
            <h1 className="text-white font-bold mt-2 ml-3">Sehat-AI</h1>
            </div>
            <div className="flex justify-between bg-white w-[434px] p-1 rounded">
                    <input className="w-full" placeholder="Enter your email">
                    </input>
                    <button className="bg-white text-black w-[70px] h-[40px] px-4 rounded-[8px] border-2 border-[#048C80] flex items-center gap-2 hover:cursor-pointer">
                    <img src={arrow} className=" border-2 border-solid border-black w-4 h-4 ml-2"></img>
                    </button>
                </div>
        </div>
        <div className='flex gap-12 px-[144px] py-[80px] '>
            <div>
                <h1 className='text-[#EFECE6]'>Product</h1>
                <ul className='flex flex-col text-[#BABABA]'>
                    <a href='#'>About</a>
                    <a href='#'>Features</a>
                    <a href='#'>Pricing</a>
                    <a href='#'>Integrations</a>
                    <a href='#'>FAQs</a>
                </ul>
            </div>
            <div>
                <h1 className='text-[#EFECE6]'>Company</h1>
                <ul className='flex flex-col text-[#BABABA]'>
                    <a href='#'>Our Story</a>
                    <a href='#'>Team</a>
                    <a href='#'>Careers</a>
                    <a href='#'>Press</a>
                    <a href='#'>Contact Us</a>
                </ul>
            </div>
            <div>
                <h1 className='text-[#EFECE6]'>Resources</h1>
                <ul className='flex flex-col text-[#BABABA]'>
                    <a href='#'>Blog</a>
                    <a href='#'>Webinars</a>
                    <a href='#'>Case Studies</a>
                    <a href='#'>Templates</a>
                    <a href='#'>Help Center</a>
                </ul>
            </div>
            <div>
                <h1 className='text-[#EFECE6]'>Legal</h1>
                <ul className='flex flex-col text-[#BABABA]'>
                    <a href='#'>Terms of Service</a>
                    <a href='#'>Privacy Policy</a>
                    <a href='#'>Cookie Policy</a>
                    <a href='#'>Acceptable Use</a>
                    <a href='#'>Refund Policy</a>
                </ul>
            </div>
        </div>
        </div>
        <div className="bg-[#048C80] h-[76px] flex justify-between items-center px-36">
            <p>@SehatAI. All Rights Reserved. @sehatai</p>
            <div className='flex gap-7'>
            <img src={facebook}></img>
            <img src={linkedin}></img>
            <img src={twitter}></img>
            <img src={youtube}></img>
            </div>
            
        </div>
        </>
    )
}
export default Footer