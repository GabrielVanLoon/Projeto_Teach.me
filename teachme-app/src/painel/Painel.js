import React from 'react';
import './Painel.css';

import { Router, Link } from "@reach/router"

function Painel() {
    return (
        <main id="page-painel" class="body-card">
            <hgroup>
                <h4>Olá NOME_USUÁRIO,</h4>
                <h1>Seja bem vindo ao Teach.me</h1>
            </hgroup>

            <section class="notifications">
                <h4><i class="fa-fw fas fa-bell"></i> Últimas Notificações</h4>
                <article>
                    <p>Lorem ipsum dolor sit amet</p>
                    <p><button class="btn btn-small btn-warning"><i class="fa-fw fas fa-times"></i></button></p>
                </article>
                <article>
                    <p>Lorem ipsum dolor sit amet</p>
                    <p><button class="btn btn-small btn-danger"><i class="fa-fw fas fa-times"></i></button></p>
                </article>
                <article>
                    <p>Lorem ipsum dolor sit amet</p>
                    <p><button class="btn btn-small btn-success"><i class="fa-fw fas fa-times"></i></button></p>
                </article>
            </section>
            
            {/* <nav>
                <h3>O que deseja fazer?</h3>
                <p class="text-center">
                    <a href="#" class="btn btn-secondary">Buscar Instrutor</a>
                    <a href="#" class="btn">Minhas Aulas</a>
                    <a href="#" class="btn">Minhas Turmas</a>
                    <a href="#" class="btn">Chat</a>
                </p>
            </nav> */}

        </main>
    );
  }
  
  export default Painel;
  