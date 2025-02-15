import arrow from '../assets/arrow.svg'
import ctaShapes from '../assets/cta-shapes.png'
const CTA = ()=>{
    return(
        <section>
            <div className='flex'>
                <div className='px-[260px] py-[90px] '>
                    <h1 className='text-4xl text-white w-[250px] py-2.5'>Unlock the Full Potential of <span className=' bg-gradient-to-bl from-[#AAD9D1] to-[#017373] bg-clip-text text-transparent'>SehatAI</span></h1>
                    <p className='text-[#BABABA] w-[470px] py-2.5'>Ready to take control of your health with AI-powered insights? Start your free trial of SehatAI today and experience the future of smart healthcare!🫀</p>
                    <button className="bg-gradient-to-bl from-[#AAD9D1] to-[#017373] text-black w-[200px] h-[56px] px-6 py-2 rounded-[8px] hover:scale-102 flex items-center gap-2 hover:cursor-pointer" onClick={()=>console.log("Hello")}>Sign Up for Free
                    <img src={arrow} className=" border-2 border-solid border-black w-4 h-4 ml-2"></img>
                    </button>
                </div>
                <div>
                    <img src={ctaShapes}></img>
                </div>
            </div>
        </section>
    )
}
export default CTA