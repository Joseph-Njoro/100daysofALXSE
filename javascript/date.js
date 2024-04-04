// dateFormatter.js

export function formatDate(date) {
    const options = {
      year: 'numeric',
      month: 'long',
      day: 'numeric',
      weekday: 'long',
      hour: '2-digit',
      minute: '2-digit',
      second: '2-digit'
    };
  
    return new Intl.DateTimeFormat('en-US', options).format(date);
  }