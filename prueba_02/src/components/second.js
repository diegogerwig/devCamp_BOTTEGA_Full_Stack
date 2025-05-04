import React from "react";

import { useState } from "react";
import { useEffect } from "react";
import { useRef } from "react";
import { useMemo } from "react";


export default function Second() {
  const [count, setCount] = useState(0);
  const [name, setName] = useState("");

  const inputRef = useRef(null);

  const handleClick = () => {
	setCount(count + 1);
  };

  useEffect(() => {
	console.log("El componente se ha montado o actualizado");
	return () => {
	  console.log("El componente se va a desmontar o actualizar");
	};
  }, [count]); // Solo se ejecuta cuando count cambia

  const memoizedValue = useMemo(() => {
	return count * 2;
  }, [count]); // Solo se recalcula cuando count cambia

  return (
	<div className="second">
	  <h5 style={{ color: 'red' }}>Hola Mundo SECOND</h5>
	  <p>Contador: {count}</p>
	  <button onClick={handleClick}>Incrementar</button>
	  <input ref={inputRef} type="text" value={name} onChange={(e) => setName(e.target.value)} />
	  <p>Valor memorizado: {memoizedValue}</p>
	</div>
  );
}