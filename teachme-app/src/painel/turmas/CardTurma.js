import React from 'react'
import './CardTurma.css';

function CardTurma(props){
    return(
        <article class="card-turma">
            <div class="turma-header">
                <img src="https://oficinadainteligencia.com.br/wp-content/uploads/2019/07/opulent-profile-square-06.jpg"/>
                <div class="title">
                    <h3>
                        <a href="#"> 
                            {props.titulo}
                            { props.ehLider && <i class="fa-fw fas fa-crown" title="Líder da turma"></i> }
                        </a>
                    </h3>
                    <p><small> {props.qtdMembros}/{props.maxMembros} participantes | Situação: {props.situacao}</small></p>
                </div>
            </div>
            <div class="turma-body">
                <p>{props.descricao || 'Nenhuma descrição disponível.'}</p>
            </div>
        </article>
    );
}

{/* <article class="card-turma">
<div class="turma-header">
    <img src="https://oficinadainteligencia.com.br/wp-content/uploads/2019/07/opulent-profile-square-06.jpg"/>
    <div class="title">
        <h3><a href="#">Grupo Cálculo 3 - Federson 2019 <i class="fa-fw fas fa-share"></i></a></h3>
        <p><small>4/5 participantes | Status: Procurando Instrutor</small></p>
    </div>
</div>
<div class="turma-body">
    <p>Aenean ac facilisis arcu, at blandit turpis. Praesent nisl ipsum, tincidunt a aliquet nec, vulputate et nibh. Etiam ac erat ut arcu accumsan ornare. Sed tortor enim, hendrerit vitae tincidunt nec, malesuada id ipsum.</p>
</div>
</article> */}



export default CardTurma;