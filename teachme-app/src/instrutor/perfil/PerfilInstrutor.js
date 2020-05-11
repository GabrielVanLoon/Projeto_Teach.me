import React from 'react';
import './PerfilInstrutor.css';

const instrutor = {
    nome:       'Maria Joaquina',
    avalizaçao: '4.5',
    formaçao:   'Graduada em Letras na USP',
    local:      'São Carlos - SP',
    texto:      'Quisque ac imperdiet dui, quis scelerisque lacus. Vivamus in tortor nunc. Etiam iaculis ut purus sit amet malesuada. Vivamus at odio laoreet, ultrices tellus eu, accumsan sapien. Duis sodales libero quam.', 
}

const disciplinas = [
    {
        nome:       'Inglês',
        preço:      'R$ 100.00',
        descriçao:  'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus rutrum at purus sit amet consequat. Nulla et orci quam. Vivamus.'
    },
    {
        nome:       'Francês',
        preço:      'R$ 60.00',
        descriçao:  'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis accumsan varius sapien, a posuere nibh dapibus eu. Duis.'
    },
    {
        nome:       'Alemão',
        preço:      'R$ 120.00',
        descriçao:  'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc eget hendrerit nunc. In sagittis, arcu nec venenatis dignissim, nibh.'
    },
]

const avaliaçoes = [
    {
        nome:       'Letícia Fernandes',
        nota:       '4.5/5',
        comentario: 'Ótima professora de Inglês. Aprendi muito com ela!',
    },
    {
        nome:       'Christian V.',
        nota:       '5/5',
        comentario: 'Conseguiu me preparar para uma entrevista de emprego na França em menos de uma semana.',
    },
    {
        nome:       'Matheus Fernandes',
        nota:       '4/5',
        comentario: 'Tive aulas de alemão online melhores.',
    },
]


function PerfilInstrutor(){

    function showCalendar(){
        return(
            <img src="https://cdn.pixabay.com/photo/2016/10/23/17/06/calendar-1763587_960_720.png"></img>
        )
    }

    function cardDisciplina(item){
        return(
            <article>
                <div class="info">
                    <h3>{ item.nome }</h3>
                    <p>{ item.descriçao }</p>
                    <p class="preço">{ item.preço }</p>
                </div>
            </article>
        );
    }

    function cardAvaliaçao(item){
        return(
            <article>
                <div class="info">
                    <h3>{ item.nome }</h3>
                    <p>{ item.nota }</p>
                    <p>{ item.comentario }</p>
                </div>
            </article>
        );
    }

    return(
        <main id="page-perfil-instrutor" class="body-card">
            <article>
                <div class="picture">
                    <img src="https://oficinadainteligencia.com.br/wp-content/uploads/2019/07/opulent-profile-square-06.jpg"/>
                </div>
                <div class="info">
                    <h3>{ instrutor.nome }</h3>
                    <p>{ instrutor.avalizaçao }</p>
                    <p>{ instrutor.formaçao }</p>
                    <p>{ instrutor.local }</p>
                    <p>{ instrutor.texto }</p>
                </div>
            </article>

            <p class="right-btn">
                <button class = "btn"><span>Iniciar conversa</span></button>
            </p>

            <nav id="tab-list">
                <li><a href="#">Horários</a></li>
                <li class="active"><a href="#">Disciplinas</a></li>
                <li><a href="#">Avaliações</a></li>
            </nav>

            {/*
            <section id="tab-calendar">
                {showCalendar()}
            </section>
            */}
            
            <section id="tab-content">
                { disciplinas.map( cardDisciplina ) }
            </section>

            {/*
            <section id="tab-content">
                { avaliaçoes.map( cardAvaliaçao ) }
            </section>
            */}

        </main>
    );
}

export default PerfilInstrutor;