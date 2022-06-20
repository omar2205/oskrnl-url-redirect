<script lang="ts">
  import { getURLFromUID } from '$lib/BackendService'

  let res = 'none'

  async function handle_form(e: any) {
    e.preventDefault()
    const formData = new FormData(e.target)
    const uuid = formData.get('url')

    const { data } = await getURLFromUID(uuid as string)
    res = data
  }
</script>

<h1>Welcome to SvelteKit</h1>
<form on:submit|preventDefault={handle_form}>
  <input type="text" name="uid" placeholder="URL" />
  <button type="submit">Get</button>
</form>

{JSON.stringify(res, null, 2)}

<style>
  :global(body) {
    margin: 0;
    padding: 0;
    font-family: 'Futura Now Headline', sans-serif;
    font-size: 4rem;
  }
</style>
