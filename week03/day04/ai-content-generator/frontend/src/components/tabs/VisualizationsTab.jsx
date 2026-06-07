import { useState } from 'react'

const CHARTS = [
  {
    id: 'interest_distribution',
    icon: '📊',
    label: 'Distribution des intérêts',
    desc: 'Seaborn · barh chart',
    file: 'interest_distribution.png',
    status: 'ready',
  },
  {
    id: 'activity_heatmap',
    icon: '🌡️',
    label: "Heatmap d'activité",
    desc: 'Seaborn · heatmap · heure × catégorie',
    file: 'activity_heatmap.png',
    status: 'ready',
  },
  {
    id: 'recommendations_chart',
    icon: '📈',
    label: 'Catégories par segment',
    desc: 'Matplotlib · grouped bar',
    file: 'recommendations_chart.png',
    status: 'pending',
  },
]

export default function VisualizationsTab() {
  const [generating, setGenerating] = useState(false)
  const [done, setDone]             = useState(false)

  const generateAll = () => {
    setGenerating(true)
    fetch('/api/visualize')
      .then(r => r.json())
      .then(() => { setGenerating(false); setDone(true) })
      .catch(() => {
        setGenerating(false)
        alert('Backend non disponible. Lance : cd backend && python api.py')
      })
  }

  return (
    <div>
      <div style={{ fontSize: 16, fontWeight: 600, marginBottom: 4 }}>Visualisations</div>
      <div style={{ fontSize: 12, color: '#73726c', marginBottom: 16 }}>
        Matplotlib · Seaborn · graphiques générés par visualizer.py dans backend/outputs/
      </div>

      <div style={{ display: 'flex', gap: 8, marginBottom: 20 }}>
        <button style={btnPrimary} onClick={generateAll} disabled={generating}>
          {generating ? '⏳ Génération…' : '▶ Générer tous les graphiques'}
        </button>
      </div>

      {/* Grille des graphiques */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: 12, marginBottom: 20 }}>
        {CHARTS.map(chart => (
          <ChartBox key={chart.id} chart={chart} done={done} />
        ))}
      </div>

      {/* Fichiers générés */}
      <div style={{ border: '1px solid rgba(0,0,0,0.07)', borderRadius: 12, padding: 16, background: '#fff' }}>
        <div style={{ fontSize: 11, fontWeight: 500, color: '#73726c', fontFamily: 'monospace', textTransform: 'uppercase', letterSpacing: '0.5px', marginBottom: 12 }}>
          Fichiers générés — backend/outputs/
        </div>
        {CHARTS.map(chart => (
          <div key={chart.id} style={{ display: 'flex', alignItems: 'center', gap: 10, marginBottom: 8, fontSize: 12 }}>
            <span style={{ fontFamily: 'monospace', color: '#73726c' }}>📄</span>
            <span style={{ fontFamily: 'monospace', flex: 1 }}>{chart.file}</span>
            <span style={{
              fontSize: 10, padding: '2px 8px', borderRadius: 20, fontFamily: 'monospace', fontWeight: 500,
              background: (chart.status === 'ready' || done) ? '#E1F5EE' : '#EEEDFE',
              color: (chart.status === 'ready' || done) ? '#085041' : '#3C3489',
            }}>
              {(chart.status === 'ready' || done) ? 'prêt' : 'en attente'}
            </span>
          </div>
        ))}
      </div>
    </div>
  )
}

function ChartBox({ chart, done }) {
  return (
    <div style={{
      border: `1px dashed ${done || chart.status === 'ready' ? '#1D9E75' : 'rgba(0,0,0,0.15)'}`,
      borderRadius: 10, height: 120,
      display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center',
      gap: 6, cursor: 'pointer', background: done || chart.status === 'ready' ? '#E1F5EE' : '#fafaf8',
      transition: 'all .2s',
    }}>
      <div style={{ fontSize: 24 }}>{chart.icon}</div>
      <div style={{ fontSize: 12, fontWeight: 500, textAlign: 'center', color: done || chart.status === 'ready' ? '#085041' : '#1a1a18' }}>
        {chart.label}
      </div>
      <div style={{ fontSize: 10, color: '#73726c', fontFamily: 'monospace' }}>{chart.desc}</div>
    </div>
  )
}

const btnPrimary = { background: '#7F77DD', color: '#fff', border: 'none', borderRadius: 8, padding: '9px 16px', fontSize: 13, fontWeight: 500, cursor: 'pointer' }
