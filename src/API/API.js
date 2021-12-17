export const getParcels = async () => {
  try {
    const result = await fetch(
      "https://9g0mcps6ra.execute-api.us-east-2.amazonaws.com/lab_4_prod"
    );
    let data = await result.json();
    data = JSON.parse(data.body)
    return data;
  } catch (e) {
    console.log(e);
  }
};

