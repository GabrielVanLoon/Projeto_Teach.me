import React from 'react';
import './Vantagens.css';


const items = [
    { src: 'https://svgsilh.com/svg/1139385.svg',
      text:'Não perca tempo! Encontre o instrutor ideal para você de forma rápida e segura.',
    },
    { src: 'https://svgsilh.com/svg/3105485.svg',
      text:'A aula fica mais divertida com mais gente! Temos opções para aulas em grupo.',
    },
    { src: 'https://svgsilh.com/svg_v2/1547551.svg',
      text:'Tenha aulas pertinho de casa! Encontramos um instrutor que atenda em locais próximos a você.',
    },
    { src: 'https://svgsilh.com/svg/1910761.svg',
      text:'Preços que cabem no seu bolso! Busque por aulas dentro de suas condições financeiras.',
    },
    { src: 'https://svgsilh.com/svg/720213.svg',
      text:'Instrutores avaliados a cada aula pelos alunos. É garantia de qualidade e compromentimento com você.',
    },
];

function Vantagens() {
  
  function renderRow(item){
    return (
      <article>
        <img src={ item.src }/>
        <p>{ item.text }</p>
      </article>
    )
  }  

  return (
    <section class="vantagens">
      { items.map(renderRow) }
    </section>
  );
}

export default Vantagens;