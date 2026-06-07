import { useState, useEffect } from 'react'

// Données de démonstration (remplacées par l'API quand Flask tourne)
const DEMO_USERS = [
  { user_id: 'U0001', name: 'Alice Martin_0',  age: 28, interests: ['technologie', 'musique'],  activity_log: ['watched AI talk', 'listened to rock music', 'bought headphones'] },
  { user_id: 'U0002', name: 'Awa Mbaye_1',     age: 34, interests: ['fitness', 'science'],      activity_log: ['completed workout', 'read science article', 'bought sports shoes'] },
  { user_id: 'U0003', name: 'Leo Kouassi_2',   age: 22, interests: ['musique', 'technologie', 'fitness'], activity_log: ['created playlist', 'tracked running', 'read tech blog'] },
  { user_id: 'U0004', name: 'Sara Nguyen_3',   age: 45, interests: ['science'],                 activity_log: ['watched documentary', 'subscribed to newsletter'] },
  { user_id: 'U0005', name: 'Nathan Bah_4',    age: 31, interests: ['voyage', 'cuisine'],       activity_log: ['searched flights', 'tried new recipe', 'booked hotel'] },
  { user_id: 'U0006', name: 'Clara Ndiaye_5',  age: 19, interests: ['musique', 'fitness'],      activity_log: ['listened to jazz', 'completed workout', 'bought protein powder'] },
]

const COLORS = {
  technologie: { bg: '#EEEDFE', color: '#3C3489' },
  musique:     { bg: '#E1F5EE', color: '#085041' },
  fitness:     { bg: '#FAEEDA', color: '#633806' },
  science:     { bg: '#FAECE7', color: '#4A1B0C' },
  voyage:      { bg: '#E6F1FB', color: '#0C447C' },
  cuisine:     { bg: '#FBEAF0', color: '#4B1528' },
}

const AVATARS = ['#EEEDFE', '#E1F5EE', '#FAEEDA', '#FAECE7', '#E6F1FB', '#FBEAF0']
const AVATAR_TEXT = ['#3C3489', '#085041', '#633806', '#4A1B0C', '#0C447C', '#4B1528']

export default function UsersTab() {
  const [users, setUsers] = useState(DEMO_USERS)
  const [loading, setLoading] = useState(false)

  const loadFromAPI = () => {
    setLoading(true)
    fetch('/api/users?per_page=6')
      .then(r => r.json())
      .then(d => { setUsers(d.users); setLoading(false) })
      .catch(() => { setLoading(false); alert('Backend non disponible. Lance python api.py') })
  }

  return (
    <div>
      <div style={{ marginBottom: 16 }}>
        <div style={{ fontSize: 16, fontWeight: 600, marginBottom: 4 }}>Profils utilisateurs</div>
        <div style={{ fontSize: 12, color: '#73726c', marginBottom: 12 }}>
          Données synthétiques · NumPy + Pandas · attributs: nom, âge, intérêts, journal d'activité
        </div>
        <div style={{ display: 'flex', gap: 8 }}>
          <button style={btnPrimary} onClick={loadFromAPI} disabled={loading}>
            {loading ? 'Chargement…' : '⟳ Charger depuis l\'API'}
          </button>
        </div>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 12 }}>
        {users.map((user, i) => (
          <UserCard key={user.user_id} user={user} index={i} />
        ))}
      </div>
    </div>
  )
}

function UserCard({ user, index }) {
  const initials = user.name.split(' ').slice(0, 2).map(n => n[0]).join('').toUpperCase().slice(0, 2)
  const ci = index % AVATARS.length

  return (
    <div style={{
      border: '1px solid rgba(0,0,0,0.07)', borderRadius: 12,
      padding: 14, background: '#fff', cursor: 'pointer',
    }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: 10, marginBottom: 10 }}>
        <div style={{
          width: 38, height: 38, borderRadius: '50%', flexShrink: 0,
          display: 'flex', alignItems: 'center', justifyContent: 'center',
          background: AVATARS[ci], color: AVATAR_TEXT[ci],
          fontSize: 13, fontWeight: 600,
        }}>
          {initials}
        </div>
        <div>
          <div style={{ fontSize: 13, fontWeight: 600 }}>{user.name.split('_')[0]}</div>
          <div style={{ fontSize: 11, color: '#73726c' }}>{user.age} ans · {user.user_id}</div>
        </div>
      </div>

      <div style={{ display: 'flex', flexWrap: 'wrap', gap: 5, marginBottom: 8 }}>
        {user.interests.map(interest => {
          const c = COLORS[interest] || { bg: '#f4f3ef', color: '#444' }
          return (
            <span key={interest} style={{
              fontSize: 10, padding: '3px 8px', borderRadius: 20,
              background: c.bg, color: c.color, fontFamily: 'monospace',
            }}>
              {interest}
            </span>
          )
        })}
      </div>

      <div style={{ fontSize: 11, color: '#9a9891', fontFamily: 'monospace' }}>
        {user.activity_log.length} activités · sim: {(0.7 + Math.random() * 0.25).toFixed(2)}
      </div>
    </div>
  )
}

const btnPrimary = { background: '#7F77DD', color: '#fff', border: 'none', borderRadius: 8, padding: '9px 16px', fontSize: 13, fontWeight: 500, cursor: 'pointer' }
