import { useState, useEffect } from 'react'
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from 'recharts'

const INTERESTS_DATA = [
  { name: 'Technologie', value: 82, color: '#7F77DD' },
  { name: 'Fitness',     value: 74, color: '#EF9F27' },
  { name: 'Musique',     value: 61, color: '#1D9E75' },
  { name: 'Science',     value: 48, color: '#D85A30' },
  { name: 'Voyage',      value: 35, color: '#888780' },
  { name: 'Cuisine',     value: 28, color: '#D4537E' },
]

const PIPELINE = [
  { step: '1', label: 'Génération',  done: true  },
  { step: '2', label: 'Nettoyage',   done: true  },
  { step: '3', label: 'Analyse',     done: true  },
  { step: '4', label: 'Moteur',      done: false },
  { step: '5', label: 'Viz',         done: false },
]

export default function DashboardTab() {
  const [status, setStatus] = useState(null)

  // Appel API Flask (quand le backend tourne)
  useEffect(() => {
    fetch('/api/status')
      .then(r => r.json())
      .then(setStatus)
      .catch(() => setStatus({ status: 'demo', users: 500 }))
  }, [])

  return (
    <div>
      {/* Stats */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: 12, marginBottom: 20 }}>
        <StatCard label="Utilisateurs"     value={status?.users ?? 500}   color="#3C3489" />
        <StatCard label="Recommandations"  value="3 200"                   color="#085041" />
        <StatCard label="Précision"        value="87%"                     color="#633806" />
        <StatCard label="Catégories"       value="6"                       color="#4A1B0C" />
      </div>

      {/* Graphique + Pipeline */}
      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 16 }}>
        <div style={card}>
          <div style={cardTitle}>Répartition des intérêts</div>
          <ResponsiveContainer width="100%" height={180}>
            <BarChart data={INTERESTS_DATA} layout="vertical">
              <XAxis type="number" domain={[0, 100]} tick={{ fontSize: 11 }} unit="%" />
              <YAxis type="category" dataKey="name" tick={{ fontSize: 12 }} width={80} />
              <Tooltip formatter={v => `${v}%`} />
              <Bar dataKey="value" radius={[0, 4, 4, 0]}>
                {INTERESTS_DATA.map((entry, i) => (
                  <rect key={i} fill={entry.color} />
                ))}
              </Bar>
            </BarChart>
          </ResponsiveContainer>
        </div>

        <div style={card}>
          <div style={cardTitle}>Pipeline de traitement</div>
          <div style={{ display: 'flex', alignItems: 'center', gap: 4, marginBottom: 16 }}>
            {PIPELINE.map((p, i) => (
              <div key={p.step} style={{ display: 'flex', alignItems: 'center', gap: 4 }}>
                <div style={{
                  width: 36, height: 36, borderRadius: '50%',
                  display: 'flex', alignItems: 'center', justifyContent: 'center',
                  fontSize: 13, fontWeight: 600,
                  background: p.done ? '#EEEDFE' : '#f1efe8',
                  color: p.done ? '#3C3489' : '#888',
                  border: `1px solid ${p.done ? '#AFA9EC' : '#ddd'}`,
                }}>
                  {p.step}
                </div>
                {i < PIPELINE.length - 1 && <span style={{ color: '#ccc', fontSize: 14 }}>→</span>}
              </div>
            ))}
          </div>
          <div style={{ fontSize: 11, color: '#73726c', fontFamily: 'monospace', marginBottom: 14 }}>
            Étapes 1–3 complètes · Étape 4 en attente
          </div>
          <div style={{ display: 'flex', gap: 8 }}>
            <button style={btnPrimary}
              onClick={() => fetch('/api/visualize').catch(() => alert('Lance d\'abord : python api.py'))}>
              ▶ Lancer le pipeline
            </button>
            <button style={btnSecondary}
              onClick={() => fetch('/api/status').then(r => r.json()).then(d => alert(JSON.stringify(d)))}>
              Statut
            </button>
          </div>
        </div>
      </div>
    </div>
  )
}

function StatCard({ label, value, color }) {
  return (
    <div style={{ background: '#f4f3ef', borderRadius: 8, padding: '14px 16px' }}>
      <div style={{ fontSize: 11, color: '#73726c', fontFamily: 'monospace', textTransform: 'uppercase', letterSpacing: '0.5px', marginBottom: 6 }}>{label}</div>
      <div style={{ fontSize: 26, fontWeight: 700, color, letterSpacing: '-1px' }}>{value}</div>
    </div>
  )
}

const card      = { border: '1px solid rgba(0,0,0,0.07)', borderRadius: 12, padding: 16, background: '#fff' }
const cardTitle = { fontSize: 11, fontWeight: 500, color: '#73726c', fontFamily: 'monospace', textTransform: 'uppercase', letterSpacing: '0.5px', marginBottom: 14 }
const btnPrimary   = { background: '#7F77DD', color: '#fff', border: 'none', borderRadius: 8, padding: '9px 16px', fontSize: 13, fontWeight: 500, cursor: 'pointer' }
const btnSecondary = { background: '#f4f3ef', color: '#1a1a18', border: '1px solid rgba(0,0,0,0.1)', borderRadius: 8, padding: '9px 16px', fontSize: 13, cursor: 'pointer' }
