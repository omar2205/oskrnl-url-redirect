const generateURL = async (url: string) => {
  const response = await fetch('/create', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ url }),
  })
  const data = await response.json()
  return data
}

const getURLFromUID = async (uuid: string) => {
  const response = await fetch(`/get_url/${uuid}`)
  const data = await response.json()
  return data
}

export { generateURL, getURLFromUID }
