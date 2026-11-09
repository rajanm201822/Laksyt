
//lue alku ja loppuvuosi

let alku = parseInt(prompt('anna alkuvuosi'));

let loppu = parseInt(prompt('anna loppuvuosi'));

 let lista = document.getElementById('lista')

for (let v = alku; v <= loppu; v += 1)

{
    //tutkitaan onko vuosi v karkausvusi

    if ((v % 4 === 0  && v % 100 !== 0) || (v % 400 === 0))

    {
        //v on karkausvuosi

        lista.innerHTML += `<li>${v}</li>`;
    }

}