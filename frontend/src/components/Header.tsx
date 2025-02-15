import React from "react";
import logo from '../assets/SehatAI_logo.jpg'
import arrow from '../assets/arrow.svg'
const Header = ()=>{
    return(
        <>
        <nav className=" flex justify-between items-center px-[96px] py-[24px] border-b-[#048C80]/50 border-1">
        <div className="flex">
            <img src={logo} width={48} className="rounded"></img>
            <h1 className="text-white font-bold mt-2 ml-3">Sehat-AI</h1>
        </div>
        <ul className="flex gap-10 text-white">
            <a href="#">Features</a>
            <a href="#">Dashboard</a>
            <a href="#">Support</a>
        </ul>
        <button className="bg-gradient-to-bl from-[#AAD9D1] to-[#017373] text-black w-[167px] h-[56px] px-6 py-2 rounded-[8px] hover:scale-102 flex items-center gap-2 hover:cursor-pointer" onClick={()=>console.log("Hello")}>Get Started
        <img src={arrow} className=" border-2 border-solid border-black w-4 h-4 ml-2"></img>
        </button>
        </nav>
        </>
    )
}
export default Header;