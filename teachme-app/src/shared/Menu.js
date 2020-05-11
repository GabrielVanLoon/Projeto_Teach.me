import React from 'react';
import './Menu.css';

import { Link } from "@reach/router"

function Menu(props) {

    function closeMenu(){
        props.setMenuState(false);
    }

    return (
        <React.Fragment>
            <div id="menu-sidebar" class={props.menuState && 'visible'}>
               <section class="logo">
                   <h2 class="text-center">Teach.me</h2>
               </section>

                <nav>
                    <li><Link to="/" onClick={closeMenu}><i class="fa-fw fas fa-home"/> Home</Link></li>
                </nav>
                <nav>
                    <li><Link to="/painel" onClick={closeMenu}><i class="fa-fw fas fa-user"/> Painel</Link></li>
                    <ul>
                        <li><Link to="/painel/meu-perfil" onClick={closeMenu}>Minha Conta</Link></li>
                        <li><Link to="/painel/turma/minhas-turmas" onClick={closeMenu}>Minhas Turmas</Link></li>
                        <li><Link to="#" onClick={closeMenu}>Minhas Aulas</Link></li>
                    </ul>
                </nav>
                <nav>
                    <li><Link to="instrutores" onClick={closeMenu}><i class="fa-fw fas fa-graduation-cap"/> Instrutores</Link></li>
                </nav>
                <nav>
                    <li><Link to="instrutores" onClick={closeMenu}><i class="fa-fw fas fa-comment"/> Chat</Link></li>
                </nav>
            </div>

            <div id="menu-shadow" class={props.menuState && 'visible'} onClick={closeMenu}>&nbsp;</div>
        </React.Fragment>
    );
}

export default Menu;