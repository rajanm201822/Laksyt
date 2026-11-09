'use strict';

/*

luetaan syöte
 */


//voi käyttää myös +
let v =parseInt(prompt('Anna vuosiluku'))

/*
 etistään html dokumentista kohta vastaukselle.
 */
let vastaus = document.querySelector('#vastaus');


/*

tutkitaan onko karkausvuosi

 */

if ((v % 4 === 0  && v % 100 !== 0) || (v % 400 === 0))

{
    /*
   on karkausvuosi
     */

    vastaus.innerHTML = `${v} on karkausvuosi`;
}
else
{
    vastaus.innerHTML = `${v} ei ole karkausvuosi`;
}