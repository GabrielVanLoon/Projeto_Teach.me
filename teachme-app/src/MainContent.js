import React from 'react';
import { Router, Link } from "@reach/router"

// General Pages
import Home     from './home/Home';
import Login    from './login/Login';
import Cadastro from './cadastro/Cadastro';

// Painel Aluno
import Painel       from './painel/Painel';
import MeuPerfil    from './painel/meu-perfil/MeuPerfil'
import MinhasTurmas from './painel/turmas/MinhasTurmas'

// Painel Instrutor

// Instrutor
import Buscar from './instrutor/Buscar'

function MainContent() {
    return (
        <Router>
            <Home     path='/' default/>
            <Login    path='/login'/>
            <Cadastro path='/criar-conta'/>
            
            <Painel       path='/painel'/>
            <MeuPerfil    path='/painel/minha-conta'/>
            <MinhasTurmas path='/painel/minhas-turmas'/>
            
            <MinhasTurmas path='/painel-instrutor/minhas-turmas' painelInstrutor={true} />


            <Buscar  path="/instrutor" />
        </Router>
    );
}

export default MainContent;