import React from 'react';
import './MinhasPropostas.css';

import CardProposta from './CardProposta'

function MinhasTurmas(props) {
    return(
        <main id="page-minhas-propostas" class="body-card">
            <h1>Aulas e Propostas</h1>

            <section class="filtros">
                <label for="filtro-status">Filtrar propostas </label>
                <select id="filtro-status" name="filtro-status">
                    <option selected>Mostrar todas</option>
                    <option>Em votação</option>
                    <option>Com aulas em curso</option>
                    <option>Finalizadas</option>
                    <option>Recusadas</option>
                </select>
            </section> 

            <section class="propostas">
                <CardProposta />
                <CardProposta />
                <CardProposta />
            </section>

        </main>
    );
}

export default MinhasTurmas;