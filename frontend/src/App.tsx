import { useState } from 'react'
import Hero from "./components/Hero"
import './App.css'
import Header from './components/Header'
import Footer from './components/Footer'
import FAQ from './components/FAQ'

function App() {

  return (
    <>
      <Header/>
      <Hero/>
      <FAQ/>
      <Footer/>
    </>
  )
}

export default App
