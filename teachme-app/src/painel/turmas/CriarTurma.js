import React from 'react';
import './CriarTurma.css';

import { Router, Link } from "@reach/router"

function CriarTurma() {
    return (
        <main id="page-criar-turma">
            <section>
                <h1>Criar Turma</h1>
            </section>
            
            <form>
                <label for="classname">Nome da Turma</label>
                <input type="text" id="classname" name="classname"/>

                <label for="descricao">Descrição</label>
                <textarea id="descricao" name="descricao"></textarea>
                
                <label for="class-size">Máximo de participantes</label>
                <input type="number" id="class-size" name="class-size"/>

                <button type="submit" class="btn">Criar Turma</button>
            </form>
        </main>
    );
  }
  
  export default CriarTurma;
  