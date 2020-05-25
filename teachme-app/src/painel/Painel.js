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
                    <p><small>24/05/2020 19:33</small><br/>Uma nova <strong>proposta</strong> aguarda sua aprovação na turma <strong><a href="#">Grupo Cálculo 3 - Federson 2019</a>.</strong></p>
                    <p><button class="btn btn-small btn-warning"><i class="fa-fw fas fa-times"></i> Fechar</button></p>
                </article>
                <article>
                    <p><small>15/05/2020 14:23</small><br/>Você foi convidado para participar na turma <strong>Grupo Cálculo 3 - Federson 2019</strong>. <strong><a href="#">Clique aqui para aceitar o convite.</a></strong></p>
                    <p><button class="btn btn-small btn-danger"><i class="fa-fw fas fa-times"></i> Fechar</button></p>
                </article>
                <article>
                    <p><small>03/05/2020 16:59</small><br/>Sua proposta com o instrutor <strong>João da Silva</strong> para a Disciplina de Cálculo foi aceita. Fique atento para os horários e locais combinados.</p>
                    <p><button class="btn btn-small btn-success"><i class="fa-fw fas fa-times"></i> Fechar</button></p>
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
  