import React from 'react';
import './App.css';

import { Router, Link } from "@reach/router"

import Header from './shared/Header';
import Footer from './shared/Footer';

import Home from      './home/Home';
import Login from     './login/Login';
import Cadastro from  './cadastro/Cadastro';

import Painel from './painel/Painel';
import MeuPerfil from './painel/meu-perfil/MeuPerfil'
import MinhasTurmas from './painel/turmas/MinhasTurmas'
import CriarTurma from './painel/turmas/CriarTurma'

function App() {
  return (
    <React.Fragment>
      <div id="body-wrapper">
        <Header/>
        
        <Router>
          <Home     path='/' default/>
          <Login    path='login'/>
          <Cadastro path='cadastro'/>
          
          <Painel       path='painel'/>
          <MeuPerfil    path='painel/meu-perfil'/>
          <MinhasTurmas path='painel/turma/minhas-turmas'/>
          <CriarTurma   path="painel/turma/criar"/>

        </Router>

        <Footer/>
      </div>
    </React.Fragment>
  );
}

export default App;
