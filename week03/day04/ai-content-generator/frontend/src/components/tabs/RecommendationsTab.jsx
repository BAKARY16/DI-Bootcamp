import { useState } from 'react'

const DEMO_RECS = [
  { titre: 'Introduction au Machine Learning',      type: 'blog',      source: 'intérêt: technologie',     score: 0.97 },
  { titre: 'Playlist : Rock classique essentiels',  type: 'playlist',  source: 'intérêt: musique',          score: 0.93 },
  { titre: 'Top 10 casques audio professionnels',   type: 'guide',     source: 'intérêt: technologie',     score: 0.88 },
  { titre: 'GPT-4 vs Gemini : comparatif 2025',    type: 'article',   source: 'utilisateur similaire',    score: 0.76 },
  { titre: 'Programme HIIT 30 minutes',             type: 'programme', source: 'utilisateur similaire',    score: 0.71 },
]

const TYPE_ICONS = {
  blog: '📚', playlist: '🎵', guide: '📖', article: '📰',
  programme: '🏋️', cours: '🎓', recette: '🍳', podcast: '🎙️',
}

export default function RecommendationsTab() {
  const [userId, setUserId]   = useState('U0001')
  const [recs, setRecs]       = useState(DEMO_RECS)
  const [loading, setLoading] = useState(false)

  const fetchRecs = () => {
    setLoading(true)
    fetch(`/api/recommend/${userId}?top_n=5`)
      .then(r => r.json())
      .then(d => { setRecs(d.recommendations); setLoading(false) })
      .catch(() => { setLoading(false); alert('Backend non disponible. Lance python api.py') })
  }

  return (
    <div>
      <div style={{ fontSize: 16, fontWeight: 600, marginBottom: 4 }}>Moteur de recommandation</div>
      <div style={{ fontSize: 12, color: '#73726c', marginBottom: 16 }}>
        OOP + similarité cosinus · scipy.spatial.distance · adapté par profil
      </div>

      {/* Sélection utilisateur */}
      <div style={{ display: 'flex', gap: 8, alignItems: 'center', marginBottom: 20 }}>
        <input
          value={userId}
          onChange={e => setUserId(e.target.value)}
          placeholder="ID utilisateur (ex: U0001)"
          style={{
            padding: '8px 12px', borderRadius: 8, border: '1px solid rgba(0,0,0,0.12)',
            fontSize: 13, fontFamily: 'monospace', width: 200,
          }}
        />
        <button style={btnPrimary} onClick={fetchRecs} disabled={loading}>
          {loading ? 'Génération…' : 'Générer les recommandations'}
        </button>
      </div>

      {/* Liste */}
      <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
        {recs.map((rec, i) => (
          <RecItem key={i} rec={rec} />
        ))}
      </div>
    </div>
  )
}

function RecItem({ rec }) {
  const icon     = TYPE_ICONS[rec.type] || '📄'
  const scoreNum = typeof rec.score === 'number' ? rec.score : parseFloat(rec.score)
  const isHigh   = scoreNum >= 0.85

  return (
    <div style={{
      display: 'flex', alignItems: 'center', gap: 12,
      border: '1px solid rgba(0,0,0,0.07)', borderRadius: 10, padding: '12px 14px', background: '#fff',
    }}>
      <div style={{
        width: 34, height: 34, borderRadius: 8, fontSize: 16,
        display: 'flex', alignItems: 'center', justifyContent: 'center',
        background: '#f4f3ef', flexShrink: 0,
      }}>
        {icon}
      </div>
      <div style={{ flex: 1 }}>
        <div style={{ fontSize: 13, fontWeight: 500, marginBottom: 2 }}>{rec.titre}</div>
        <div style={{ fontSize: 11, color: '#73726c' }}>{rec.type} · {rec.source}</div>
      </div>
      <div style={{
        fontSize: 11, fontFamily: 'monospace', fontWeight: 500,
        padding: '3px 10px', borderRadius: 20,
        background: isHigh ? '#E1F5EE' : '#EEEDFE',
        color: isHigh ? '#085041' : '#3C3489',
      }}>
        {Math.round(scoreNum * 100)}%
      </div>
    </div>
  )
}

const btnPrimary = { background: '#7F77DD', color: '#fff', border: 'none', borderRadius: 8, padding: '9px 16px', fontSize: 13, fontWeight: 500, cursor: 'pointer' }
