const FAQ = ()=>{
    return(
            
        <section className="px-[320px] py-[96px]">
        <h2 className="text-white text-5xl text-center py-[20px]">Frequently Asked <span className=" bg-gradient-to-bl from-[#AAD9D1] to-[#017373] bg-clip-text text-transparent">Questions</span></h2>
        <p className="text-[#BABABA] text-center py-[20px]">We've compiled a list of the most frequently asked questions about SehatAI to help you get the information you need. If you have any other questions, feel free to reach out to our support team.</p>
        
        <details>
            <summary className="text-[#EFECE6] rounded px-5 border-1 border-[#017373] py-5 m-5">What is SehatAI?</summary>
            <div className="bg-[#EFECE6] rounded px-5 border-1 border-[#017373] py-5 m-5">
            <p>SehatAI is an AI-powered platform that provides health insights and personalized care recommendations.</p>

            </div>
        </details>
        
        <details>
            <summary className="text-[#EFECE6] rounded px-5 border-1 border-[#017373] py-5 m-5">How does SehatAI work?</summary>
            <div className="bg-[#EFECE6] rounded px-5 border-1 border-[#017373] py-5 m-5">
            <p>SehatAI uses machine learning to analyze health data and offer actionable insights.</p>
            </div>
        </details>
        
        <details>
            <summary className="text-[#EFECE6] rounded px-5 border-1 border-[#017373] py-5 m-5">Is SehatAI free to use?</summary>
            <div className="bg-[#EFECE6] rounded px-5 border-1 border-[#017373] py-5 m-5">
            <p>Yes! SehatAI offers a free basic version with premium features available.</p>
            </div>
        </details>
        </section>

       
    )
}
export default FAQ