<script>
  import { onMount } from "svelte";
  import Crossword from "./Crossword.svelte";
  
  let dataNYTDaily = [];
  
  onMount(async () => {
    try {
      const response = await fetch('/data/nyt-daily.json');
      if (response.ok) {
        dataNYTDaily = await response.json();
      } else {
        console.error('Failed to load crossword data');
      }
    } catch (error) {
      console.error('Error loading crossword data:', error);
    }
  });
</script>

<main>
  <h1>Crossword</h1>
  <p>A NYT daily puzzle with all default settings.</p>
  
  <Crossword data={dataNYTDaily} />
</main>

<style>
  main {
    text-align: center;
    padding: 1em;
    max-width: 1200px;
    margin: 0 auto;
  }

  h1 {
    color: #ff3e00;
    text-transform: uppercase;
    font-size: 4em;
    font-weight: 100;
  }

  @media (min-width: 640px) {
    main {
      max-width: none;
    }
  }
</style>
