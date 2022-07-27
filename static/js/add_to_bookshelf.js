const addBtns = document.querySelectorAll('.add-btn')
const bookInput = document.getElementById('book-input')

addBtns.forEach(btn => {
	btn.onclick = () => {
		const bookId=btn.dataset.book;
		bookInput.setAttribute('value', bookId)
	}
})