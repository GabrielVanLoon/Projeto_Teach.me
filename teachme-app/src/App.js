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

  // Definindo os estados da aplicação
  const [menu, setMenu] = useState(false);

  return (
    <React.Fragment>
      
      <div id="body-wrapper">
        <Header menuState={menu} setMenuState={setMenu} />
        <MainContent/>    
        <Footer/>
      </div>

      <Menu menuState={menu} setMenuState={setMenu} />
      
    </React.Fragment>
  );
}

export default App;
