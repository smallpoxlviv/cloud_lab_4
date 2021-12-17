export const getParcels = async () => {
  try {
    const result = await fetch(
      "conta-LoadB-1JJOY4P1PQKB8-bd748dc8a22dc856.elb.us-east-1.amazonaws.com/api"
    );
    let data = await result.json();
    data = JSON.parse(data.body)
    return data;
  } catch (e) {
    console.log(e);
  }
};

