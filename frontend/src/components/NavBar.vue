<script setup>
import { onMounted } from 'vue';

onMounted(() => {
  // Carregar scripts do MDB UI Kit após a montagem do componente
  const script1 = document.createElement('script');
  script1.src = 'https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/6.4.2/mdb.min.js';
  script1.async = true;
  document.head.appendChild(script1);

  const script2 = document.createElement('script');
  script2.src = 'https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/6.4.2/js/dropdown.js'; // ajuste o caminho conforme necessário
  script2.async = true;
  document.head.appendChild(script2);
});
</script>

<template>
    <nav class="navbar navbar-expand-lg navbar-light bg-body-tertiary">
    <div class="container-fluid">
        <!-- Busca -->
        <a class="navbar-brand">Navbar</a>
        <form class="d-flex input-group w-auto">
        <input
            type="search"
            class="form-control rounded"
            placeholder="Search"
            aria-label="Search"
            aria-describedby="search-addon"
        />
        <span class="input-group-text border-0" id="search-addon">
            <i class="fas fa-search"></i>
        </span>
        </form>

        <!-- Ícone de Dropdown do Usuário -->
        <li class="nav-item me-3 me-lg-0 dropdown">
        <a
            data-mdb-dropdown-init
            class="nav-link dropdown-toggle"
            href="#"
            id="userDropdown"
            role="button"
            aria-expanded="false"
        >
            <i class="fas fa-user"></i>
        </a>
        <ul class="dropdown-menu" aria-labelledby="userDropdown">
            <li>
            <a class="dropdown-item" href="#">Action</a>
            </li>
            <li>
            <a class="dropdown-item" href="#">Another action</a>
            </li>
            <li><hr class="dropdown-divider" /></li>
            <li>
            <a class="dropdown-item" href="#">Something else here</a>
            </li>
        </ul>
        </li>
    </div>
    </nav>
</template>

