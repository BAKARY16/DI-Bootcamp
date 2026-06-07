import { useState, useEffect } from 'react'

const DEMO_STATS = {
  frequencies: {
    technologie: 0.82, fitness: 0.74, musique: 0.61,
    science: 0.48, voyage: 0.35, cuisine: 0.28,
  },
  chi2_results: [
    { paire: 'AI talk → technologie', chi2: 18.42, p_value: 0.0001, significatif: true },
    { paire: 'Rock music → musique',  chi2: 12.88, p_value: 0.0032, significatif: true },
    { paire: 'Workout → fitness',     chi2: 9.14,  p_value: 0.0271, significatif: true },
    { paire: 'Science → newsletter',  chi2: 3.20,  p_value: 0.2016, significatif: false },
  ],
}

export default function AnalyticsTab() {
  const [stats, setStats] = useState(DEMO_STATS)

  const loadStats = () => {
    fetch('/api/stats')
      .then(r => r.json())
      .then(setStats)
      .catch(() => alert('Backend non disponible. Lance python api.py'))
  }

  return (
    <div>
      <div style={{ fontSize: 16, fontWeight: 600, marginBottom: 4 }}>Analyse statistique</div>
      <div style={{ fontSize: 12, color: '#73726c', marginBottom: 16 }}>
        SciPy stats · distributions de probabilité · test χ² (chi-carré)
      </div>

      <button style={{ ...btnPrimary, marginBottom: 20 }} onClick={loadStats}>
        ↻ Charger depuis l'API
      </button>

      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 16 }}>

        {/* Test χ² */}
        <div style={card}>
          <div style={cardTitle}>Test χ² — activités vs intérêts</div>
          <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: 12 }}>
            <thead>
              <tr>
                {['Paire', 'χ²', 'p-value', 'Résultat'].map(h => (
                  <th key={h} style={{ textAlign: 'left', padding: '6px 8px', color: '#73726c', borderBottom: '1px solid rgba(0,0,0,0.07)', fontFamily: 'monospace', fontSize: 11 }}>{h}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {stats.chi2_results.map((r, i) => (
                <tr key={i}>
                  <td style={td}>{r.paire}</td>
                  <td style={{ ...td, fontFamily: 'monospace' }}>{r.chi2}</td>
                  <td style={{ ...td, fontFamily: 'monospace' }}>{r.p_value}</td>
                  <td style={td}>
                    <span style={{
                      fontSize: 11, padding: '2px 8px', borderRadius: 20,
                      background: r.significatif ? '#E1F5EE' : '#f4f3ef',
                      color: r.significatif ? '#085041' : '#73726c',
                      fontFamily: 'monospace',
                    }}>
                      {r.significatif ? '✓ Sig.' : '— Non sig.'}
                    </span>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>

        {/* Distribution */}
        <div style={card}>
          <div style={cardTitle}>Fréquence des intérêts (SciPy)</div>
          {Object.entries(stats.frequencies).map(([interest, freq]) => (
            <div key={interest} style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 8 }}>
              <div style={{ width: 90, fontSize: 12, color: '#73726c' }}>{interest}</div>
              <div style={{ flex: 1, height: 8, background: '#f4f3ef', borderRadius: 4, overflow: 'hidden' }}>
                <div style={{ width: `${freq * 100}%`, height: '100%', background: '#7F77DD', borderRadius: 4 }} />
              </div>
              <div style={{ fontSize: 11, fontFamily: 'monospace', color: '#73726c', width: 36, textAlign: 'right' }}>
                {(freq * 100).toFixed(0)}%
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}

const card      = { border: '1px solid rgba(0,0,0,0.07)', borderRadius: 12, padding: 16, background: '#fff' }
const cardTitle = { fontSize: 11, fontWeight: 500, color: '#73726c', fontFamily: 'monospace', textTransform: 'uppercase', letterSpacing: '0.5px', marginBottom: 14 }
const td        = { padding: '8px 8px', borderBottom: '1px solid rgba(0,0,0,0.05)', fontSize: 12 }
const btnPrimary = { background: '#7F77DD', color: '#fff', border: 'none', borderRadius: 8, padding: '9px 16px', fontSize: 13, fontWeight: 500, cursor: 'pointer' }
