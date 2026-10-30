const form = document.querySelector('#form');
const field = document.querySelector('#message');
const messages = document.querySelector('#messages');
function addBubble(text, who) { const bubble = document.createElement('div'); bubble.className = `bubble ${who}`; bubble.textContent = text; messages.append(bubble); messages.scrollTop = messages.scrollHeight; }
async function ask(question) {
  if (!question.trim()) return;
  addBubble(question, 'user'); field.value = '';
  try { const response = await fetch('/ask', {method: 'POST', headers: {'Content-Type':'application/json'}, body: JSON.stringify({message: question})}); const data = await response.json(); addBubble(data.answer, 'bot'); }
  catch { addBubble('Sorry, the chatbot could not respond. Is the server running?', 'bot'); }
}
form.addEventListener('submit', event => { event.preventDefault(); ask(field.value); });
document.querySelectorAll('.suggestion').forEach(button => button.addEventListener('click', () => ask(button.textContent)));
