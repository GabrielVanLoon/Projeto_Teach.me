import React from 'react';
import  { useState } from 'react'
import './App.css';

// Componentes de Alta Ordem.
import Header from './shared/Header';
import Footer from './shared/Footer';
import Menu from './shared/Menu';
import MainContent from './MainContent'

import Home from      './home/Home';
import Login from     './login/Login';
import Cadastro from  './cadastro/Cadastro';

// Estados utilizados

function App() {
  return (
    <React.Fragment>
      
      <div id="body-wrapper">
        <Header/>
        <MainContent/>    
        <Footer/>
      </div>

      <Menu/>
      
    </React.Fragment>
  );
}

export default App;
