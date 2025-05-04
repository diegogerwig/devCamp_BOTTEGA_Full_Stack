import React from 'react';
import { useState } from 'react';

import Second from './second';

export default function First() {
  const [count, setCount] = useState(0);

  return (
	<><div className="first">
		  <h3>Hola Mundo FIRST</h3>
		  <p>Contador: {count}</p>
		  <button onClick={() => setCount(count + 1)}>Incrementar</button>
	  </div><Second count={count} setCount={setCount} /></>
  );
}
