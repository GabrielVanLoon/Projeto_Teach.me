import React from 'react';
import './MinhasTurmas.css';

import CardTurma from './CardTurma'

function MinhasTurmas() {
    return (
        <main id="page-minhas-turmas" class="body-card">
            <h1>Minhas Turmas</h1>

            <section class="filtros">
                <label for="filtro-status">Filtrar status </label>
                <select id="filtro-status" name="filtro-status">
                    <option selected>Mostrar todas</option>
                    <option>Procurando Instrutor</option>
                    <option>Com aulas em curso</option>
                    <option>Removidas</option>
                </select>
            </section>

            <section class="turmas">
                <CardTurma/>
                <CardTurma/>
                <CardTurma/>
            </section>

            <section class="criar-turma">
                <form>
                    <div class="form-line">
                        <div class="form-group">
                            <label for="titulo">Título da turma</label>
                            <input type="text" id="titulo" name="titulo"/>    
                        </div>

                        <div class="form-group">
                            <label for="max_participantes">Limite de participantes</label>
                            <input type="number" id="max_participantes" name="max_participantes"  min="2" max="30"/>
                        </div>
                    </div>

                    <div class="form-group">
                        <label for="descricao">Descrição da turma</label>
                        <textarea id="descricao" name="descricao"></textarea>
                    </div>

                    <div class="form-group">
                        <p class="text-right"><button class="btn"><i class="fa-fw fas fa-plus"></i> Criar Nova Turma</button></p>
                    </div>
                </form>
            </section>

        </main>
    );
  }
  
  export default MinhasTurmas;
  