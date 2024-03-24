import './entete.css'

function Entete({text}) {
  return (
    <div className="Entete">
      Network analyse by <strong>{text}</strong>
    </div>
  );
}

export default Entete;
