import React from 'react';
import './App.css';

import { Router, Link } from "@reach/router"

import Header from './shared/Header';
import Footer from './shared/Footer';

import Home from      './home/Home'
import Login from     './login/Login'
import Cadastro from  './cadastro/Cadastro'

function App() {
  return (
    <React.Fragment>
      <div id="body-wrapper">
        <Header/>
        
        <Router>
          <Home  path='/'/>
          <Login path='login'/>
          <Cadastro path='cadastro'/>
        </Router>

        <Footer/>
      </div>
    </React.Fragment>
  );
}

export default App;
