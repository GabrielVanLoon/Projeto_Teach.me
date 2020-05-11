import React from 'react';
import { Router, Link } from "@reach/router"

import Home from      './home/Home';
import Login from     './login/Login';
import Cadastro from  './cadastro/Cadastro';

import Painel from './painel/Painel';
import MeuPerfil from './painel/meu-perfil/MeuPerfil'
import MinhasTurmas from './painel/turmas/MinhasTurmas'
import CriarTurma from './painel/turmas/CriarTurma'

import Buscar from './instrutor/Buscar'

function MainContent() {
    return (
        <Router>
            <Home     path='/' default/>
            <Login    path='login'/>
            <Cadastro path='cadastro'/>
            
            <Painel       path='painel'/>
            <MeuPerfil    path='painel/meu-perfil'/>
            <MinhasTurmas path='painel/turma/minhas-turmas'/>
            <CriarTurma   path="painel/turma/criar"/>

            <Buscar  path="instrutores" />
        </Router>
    );
}

export default MainContent;