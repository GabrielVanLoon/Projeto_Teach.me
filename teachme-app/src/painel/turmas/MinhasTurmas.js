import React from 'react';
import './MinhasTurmas.css';

import { Router, Link } from "@reach/router"

function MinhasTurmas() {
    return (
        <main id="page-minhas-turmas">
            <section>
                <h1>Minhas Turmas</h1>
                <p>Ainda não possui nenhuma turma? Crie agora mesmo!!</p>
                <button class="btn">Criar Turma</button>
            </section>
            
            <article>
                <h4>Time da Nasa</h4>
                <p><small>4/5 participantes</small></p>
                <p>Grupo de estudos de conversação em inglês.</p>
            </article>

            <article>
                <h4>Time da Nasa</h4>
                <p><small>4/5 participantes</small></p>
                <p>Grupo de estudos de conversação em inglês.</p>
            </article>
        </main>
    );
  }
  
  export default MinhasTurmas;
  