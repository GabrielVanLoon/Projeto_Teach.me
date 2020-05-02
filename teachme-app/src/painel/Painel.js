import React from 'react';
import './Painel.css';

import { Router, Link } from "@reach/router"

function Painel() {
    return (
        <main id="page-painel">
            <section>
                <h3>Olá NOME_USUÁRIO.</h3>
                <h2>Bem vindo ao Teach.me</h2>
            </section>

            <section>
                <h3>Notificações</h3>
            </section>
            
            <nav>
                <h3>O que deseja fazer?</h3>
                <a href="#" class="btn">Ver Perfil</a>
                <a href="#" class="btn">Buscar instrutor</a>
                <a href="#" class="btn">Minhas aulas</a>
                <a href="#" class="btn">Minhas turmas</a>
                <a href="#" class="btn">Chat</a>
            </nav>

        </main>
    );
  }
  
  export default Painel;
  